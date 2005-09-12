Name: stata9-license-nsfitr3usr
License: Commercial
Group: Application/Statistics
Summary: Stata 9 license from Stata.com for CISER 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 9.0
Release: 0 
Requires: stata9 >= 9.0
Source0: stata9-nsfitr.lic 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
This is the Linux64 Stata license for the NSF-ITR project (3 users). You will need to install it before initializing Stata.

%prep

%build

%install
cd %buildroot
install -d -m 755 -g root -o root %buildroot/usr/local/stata9
install -m 755 -g root -o root %{SOURCE0} %buildroot/usr/local/stata9/stata.lic

%clean

%files
/usr/local/stata9/stata.lic

%changelog
* Wed Jun 22 2005 lars.vilhuber@cornell.edu
- License for NSF-ITR
