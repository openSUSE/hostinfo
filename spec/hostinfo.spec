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
Requires:     iproute2
Requires:     issue-generator
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
mkdir -p %{buildroot}%{_sysconfdir}/cron.hourly
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_presetdir}
install -d %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{_docdir}/%{name}
install -d %{buildroot}/var/spool/%{name}
install -m 644 conf/hostinfo.conf %{buildroot}%{_sysconfdir}
install -m 444 man/COPYING.GPLv2 %{buildroot}%{_docdir}/%{name}
install -m 644 bin/10-hostinfo.preset %{buildroot}%{_presetdir}
install -m 644 bin/hostinfo.service %{buildroot}%{_unitdir}
install -m 755 bin/hostinfo %{buildroot}%{_sbindir}
install -m 755 bin/hostinfo-refresh %{buildroot}%{_sysconfdir}/cron.hourly
install -m 644 man/*.8.gz %{buildroot}%{_mandir}/man8

%files
%defattr(-,root,root)
%{_sbindir}/hostinfo
%{_unitdir}/hostinfo.service
%{_presetdir}/10-hostinfo.preset
%config %{_sysconfdir}/hostinfo.conf
%{_sysconfdir}/cron.hourly/hostinfo-refresh
%{_mandir}/man8/*
%dir %attr(0700,root,root) /var/spool/%{name}
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*

%preun
rm -f /etc/issue.d/99-hostinfo.conf
issue-generator

%changelog

