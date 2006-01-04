Name: asreml-license-ciser
License: Commercial
Group: Application/Statistics
Summary: ASReml license from vsn-int.com for CISER 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1.10
Release: 0 
Requires: asreml >= 1.10
Source0: ASReml.ciser.alx
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
This is the Linux64 ASReml license for CISER (site license).
%prep

%build

%install
cd %buildroot
install -d -m 755 -g root -o root %buildroot/usr/local/etc/asreml
install -m 755 -g root -o root %{SOURCE0} %buildroot/usr/local/etc/asreml/ASReml.alx

%clean

%files
/usr/local/etc/asreml/ASReml.alx

%changelog
* Wed Jan 6 2006 lars.vilhuber@cornell.edu
- License for CISER
