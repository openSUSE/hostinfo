# 
# spec file for package hostinfo
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:         hostinfo
Version:      1.0
Release:      0
Summary:      Gathers basic server information
License:      GPL-2.0
URL:          https://github.com/g23guy/hostinfo
Group:        System/Monitoring
Source:       %{name}-%{version}.tar.gz
Requires:     cron
Requires:     sed
Buildarch:    noarch

%description
A script that displays current system information to help 
identify a host and it's resources.
 
%prep
%setup -q

%build
gzip -9f man/*8

%install
pwd;ls -la
mkdir -p %{buildroot}%{_sysconfdir}/cron.daily
mkdir -p %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{_docdir}/%{name}
install -d %{buildroot}/var/spool/%{name}
install -m 644 conf/hostinforc %{buildroot}%{_sysconfdir}
install -m 444 man/COPYING.GPLv2 %{buildroot}%{_docdir}/%{name}
install -m 755 bin/hostinfo %{buildroot}%{_sbindir}
install -m 755 bin/hostinfo-refresh %{buildroot}%{_sysconfdir}/cron.daily
install -m 644 man/*.8.gz %{buildroot}%{_mandir}/man8

%files
%defattr(-,root,root)
%{_sbindir}/hostinfo
%config %{_sysconfdir}/hostinforc
%{_sysconfdir}/cron.daily/hostinfo-refresh
%{_mandir}/man8/*
%dir %attr(0700,root,root) /var/spool/%{name}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*

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

