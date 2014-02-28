# spec file for package hostinfo
#
# Copyright (c) 2014 SUSE LLC
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Name:         hostinfo
Summary:      Gathers basic server information
URL:          https://bitbucket.org/g23guy/hostinfo
Group:        Documentation/SUSE
License:      GPL-2.0
Autoreqprov:  on
Version:      1.0
Release:      9
Source:       %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}
Buildarch:    noarch
Requires:     cron
Requires:     sed

%description
A script that displays current system information to help 
identify a host and it's resources.

Authors:
--------
    Jason Record <jrecord@suse.com>
 
 
%prep
%setup -q

%build
gzip -9f man/*8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc
install -d $RPM_BUILD_ROOT/etc/cron.daily
install -d $RPM_BUILD_ROOT/usr/sbin
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -d $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -d $RPM_BUILD_ROOT/var/spool/%{name}
install -m 644 conf/hostinforc $RPM_BUILD_ROOT/etc
install -m 444 man/COPYING.GPLv2 $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -m 755 bin/hostinfo $RPM_BUILD_ROOT/usr/sbin
install -m 755 bin/hostinfo-refresh $RPM_BUILD_ROOT/etc/cron.daily
install -m 644 man/*.8.gz $RPM_BUILD_ROOT/usr/share/man/man8

%files
%defattr(-,root,root)
/usr/sbin/*
%config /etc/*
/etc/cron.daily/*
/usr/share/man/man8/*
%dir %attr(0700,root,root) /var/spool/%{name}
%dir /usr/share/doc/packages/%{name}
%doc /usr/share/doc/packages/%{name}/*

%post
echo '[[ -s /var/spool/hostinfo/root-motd ]] && cat /var/spool/hostinfo/root-motd' >> /root/.profile
echo "Run hostinfo" > /var/spool/hostinfo/root-motd

%preun
rm -f /var/spool/hostinfo/root-motd

%postun
if [[ -e /root/.profile ]]
then
	sed -i -e '/\/var\/spool\/hostinfo\/root-motd/d' /root/.profile
	if [[ ! -s /root/.profile ]]
	then
		rm -f /root/.profile
	fi
fi

%changelog

