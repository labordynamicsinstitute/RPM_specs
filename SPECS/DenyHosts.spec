%define name DenyHosts
%define version 2.6
%define release 2SUSE_python25

Summary: DenyHosts is a utility to help sys admins thwart ssh hackers
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPL v2
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
Vendor: Phil Schwartz <phil_schwartz@users.sourceforge.net>
Url: http://denyhosts.sourceforge.net
Patch0: DenyHosts-2.6-SUSE.patch

%description

DenyHosts is a python program that automatically blocks ssh attacks by adding entries to 
/etc/hosts.deny. DenyHosts will also inform Linux administrators about offending hosts, attacked 
users and suspicious logins.
      

%prep
%setup
%patch0 -p1

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
# SUSE specific setup
install -d  %buildroot/etc
install -d  %buildroot/etc/init.d
install denyhosts.cfg-SUSE $RPM_BUILD_ROOT/etc/denyhosts.cfg
install daemon-control-dist $RPM_BUILD_ROOT/etc/init.d/denyhosts
cat >>INSTALLED_FILES << EOF
/etc/init.d/denyhosts
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%config /etc/denyhosts.cfg
