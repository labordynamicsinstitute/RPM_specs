Name: asreml-license-nsf01
License: Commercial
Group: Application/Statistics
Summary: ASReml license from vsn-int.com for NSF01 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1.10
Release: 2 
Requires: asreml >= 1.10
Source0: nsf01.ali
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
This is the Linux64 ASReml license for NSF01.
%prep

%build

%install
cd %buildroot
install -d %buildroot/usr/local/etc/asreml
install %{SOURCE0} %buildroot/usr/local/etc/asreml/

%post
export ASREML_LICENSE_FILE=/usr/local/etc/asreml/ASReml.alx
cd /usr/local/etc/asreml
/usr/local/bin/ASREML110 -n %{SOURCE0}

%clean

%files
%defattr(0755,root,root,0755)
/usr/local/etc/asreml/nsf01.ali

%changelog
* Wed Nov 28 2007 lars.vilhuber@cornell.edu
- fixed a hanging move command
* Wed May 24 2006 lars.vilhuber@cornell.edu
- made the license rpm work with the .ali file
* Wed Jan 6 2006 lars.vilhuber@cornell.edu
- License for NSF01
