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
Group:        Documentation/SuSE
License:      GPL-2.0
Autoreqprov:  on
Version:      1.0
Release:      6
Source:       %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}
Buildarch:    noarch

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
install -d $RPM_BUILD_ROOT/usr/sbin
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -d $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -d $RPM_BUILD_ROOT/usr/lib/%{name}
install -m 644 conf/hostinforc $RPM_BUILD_ROOT/etc
install -m 444 man/COPYING.GPLv2 $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -m 755 bin/* $RPM_BUILD_ROOT/usr/sbin
install -m 644 man/*.8.gz $RPM_BUILD_ROOT/usr/share/man/man8

%files
%defattr(-,root,root)
/usr/sbin/*
/etc/*
/usr/share/man/man8/*
%dir /usr/lib/%{name}
%dir /usr/share/doc/packages/%{name}
%doc /usr/share/doc/packages/%{name}/*

%post
echo 'hostinfo # Installed by hostinfo package' >> /root/.profile
if [[ -d /etc/cron.daily ]]
then
	ln -sf /usr/sbin/hostinfo-updates /etc/cron.daily
fi

%postun
if [[ -e /root/.profile ]]
then
	sed -i -e '/^hostinfo #/d' /root/.profile
	if [[ ! -s /root/.profile ]]
	then
		rm -f /root/.profile
	fi
fi
rm -rf /usr/lib/%{name}
if [[ -L /etc/cron.daily/hostinfo-updates ]]
then
	rm -f /etc/cron.daily/hostinfo-updates
fi

%changelog

