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
Release:      1
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
install -d $RPM_BUILD_ROOT/usr/sbin
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -d $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -m 444 man/COPYING.GPLv2 $RPM_BUILD_ROOT/usr/share/doc/packages/%{name}
install -m 755 bin/* $RPM_BUILD_ROOT/usr/sbin
install -m 644 man/*.8.gz $RPM_BUILD_ROOT/usr/share/man/man8

%files
%defattr(-,root,root)
/usr/sbin/*
/usr/share/man/man8/*
%doc /usr/share/doc/packages/%{name}/*

%changelog

