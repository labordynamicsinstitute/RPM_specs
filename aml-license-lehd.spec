Name: aml-license-lehd
License: Commercial
Group: Application/Statistics
Summary: aML license for LEHD
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2.80
Release: 0 
Requires: aml >= 2.00
Source0: aml.lic.census
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
This is the Linux64 aML license for LEHD (site license).
%prep

%build

%install
cd %buildroot
install -d -m 755 -g root -o root %buildroot/usr/local/bin
install -m 755 -g root -o root %{SOURCE0} %buildroot/usr/local/bin/aml.lic

%clean

%files
/usr/local/bin/aml.lic

%changelog
* Fri Jan 13 2006 lars.vilhuber@cornell.edu
- License for LEHD
