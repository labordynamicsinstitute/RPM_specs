Summary: Tools to configure a VirtualRDC 
Name: virtualrdc_admin 
Version: 1.0.5
Release: 0
Copyright: GPL
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Source0: virtualrdc_admin-%{version}.tgz
BuildArch: noarch
Requires: perl, mysql-client


%description
* Provides tools to create user accounts, reset passwords
* Provides tools to create groups

%prep 
%setup  

%build

%install

install -d -m 755 %buildroot/usr/local/sbin
install -d -m 755 %buildroot/usr/local/bin
install -m 755 convert_phonetics.pl  %buildroot/usr/local/bin
install -m 755 vrdc.*   %buildroot/usr/local/sbin


%clean

%files
%defattr(-,root,root) 
/usr/local/bin/convert_phonetics.pl
/usr/local/sbin/vrdc.setup
/usr/local/sbin/vrdc.resetpass
/usr/local/sbin/vrdc.addusers
/usr/local/sbin/vrdc.creategroups


%changelog
* Mon Jan 10 2006 vilhuber
  - Maintenance release
  - added vrdc.setup
* Mon Feb 21 2005 vilhuber
  - fixes email address domain
* Sat Feb 19 2005 vilhuber
  - first version
