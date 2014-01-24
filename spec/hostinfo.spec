# Copyright (C) 2014 SUSE LLC
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

Name:         hostinfo
Summary:      Gathers basic server information
URL:          https://bitbucket.org/g23guy/hostinfo
Group:        Documentation/SuSE
Distribution: SUSE Linux Enterprise
Vendor:       SUSE Support
License:      GPL-2.0
Autoreqprov:  on
Version:      0.9
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
gzip -9f man/*

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/sbin
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 755 bin/* $RPM_BUILD_ROOT/usr/sbin
install -m 644 man/*.8.gz $RPM_BUILD_ROOT/usr/share/man/man8

%files
%defattr(-,root,root)
/usr/sbin/*
/usr/share/man/man8/*

%post
DATEADDED=`date +%D\ %T`
TMPFILE='/tmp/hostinfo.tmp.cijAkjd283l13'
STMP=`basename $TMPFILE`

SHELLS="/root/.bashrc"
for THISHELL in $SHELLS
do
  test -e $THISHELL && sed -i -e '/^alias hi=/d' -e '/^# Added by hostinfo/d' $THISHELL
  echo "# Added by hostinfo RPM on $DATEADDED" >> $THISHELL
  echo "alias hi='clear; hostinfo'" >> $THISHELL
  echo "hostinfo" >> $THISHELL
done

%changelog
* Fri Jan 24 2014 jrecord@suse.com
- added kernel taint and install time
- initial

