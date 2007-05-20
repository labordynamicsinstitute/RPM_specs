%define name DenyHosts
%define version 2.6
%define release 2

Summary: DenyHosts is a utility to help sys admins thwart ssh hackers
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
License: GPL v2
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
Vendor: Phil Schwartz <phil_schwartz@users.sourceforge.net>
Url: http://denyhosts.sourceforge.net

%description

DenyHosts is a python program that automatically blocks ssh attacks by adding entries to 
/etc/hosts.deny. DenyHosts will also inform Linux administrators about offending hosts, attacked 
users and suspicious logins.
      

%prep
%setup

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
