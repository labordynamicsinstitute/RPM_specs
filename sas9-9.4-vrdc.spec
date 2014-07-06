Name: sas94
License: Commercial
Group: Applications/Statistics
Summary: SAS 9.4 
Packager: Lars Vilhuber
Version: 9.4
Release: 2
Source0: sasv94_local.cfg
Source1: SAS94-desktop.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Provides: sas

%description
Manages installation of SAS. 

%package desktop
Group: Applications/Statistics
BuildArch: noarch
Summary: SAS %{version} desktop links
%description desktop
Creates links and desktop icons for SAS.

%package mkdefault
Group: Applications/Statistics
BuildArch: noarch
Summary: Make SAS %{version} the default  
%description mkdefault
Creates links for SAS %{version}

%prep

%build

%install
# install the base SAS
install -d %buildroot/opt/SAS_%{version}/SASFoundation/%{version}/
install -d %buildroot/usr/local/bin
cd %buildroot/opt/SAS_%{version}/SASFoundation/%{version}/
#[[ -f sas ]] || touch sas
install %{SOURCE0} %buildroot/opt/SAS_%{version}/SASFoundation/%{version}/sasv9_local.cfg
touch %buildroot/usr/local/bin/sas94
touch %buildroot/usr/local/bin/sas9
touch %buildroot/usr/local/bin/sas



# install the desktop stuff 
install -d %buildroot/usr/share/applications/vrdc
cd %buildroot
tar xf %{SOURCE1}

%post 
ln -sf /opt/SAS_%{version}/SASFoundation/%{version}/sas /usr/local/bin/sas94

%post mkdefault
ln -sf /usr/local/bin/sas94 /usr/local/bin/sas9
ln -sf /usr/local/bin/sas9 /usr/local/bin/sas

%preun

%postun 
rm -f /usr/local/bin/sas94

%postun mkdefault
rm -f /usr/local/bin/sas9
rm -f /usr/local/bin/sas

%clean

%files
%defattr(755,root,root)

%config
/opt/SAS_%{version}/SASFoundation/%{version}/sasv9_local.cfg
/usr/local/bin/sas94

%files desktop
%defattr(755,root,root)
/usr/share/applications/vrdc/SAS94.desktop

%files mkdefault
%defattr(755,root,root)
/usr/local/bin/sas9
/usr/local/bin/sas


%changelog
* Tue Jun  3 2014 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.4
- SAS 9.4

* Mon Dec  7 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.2-5
- Moved the desktop files to compliant location in /usr/share/applications/

* Tue Feb 10 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.2-1
- For 9.2, removed the actual installed files (too big)

* Mon Feb  9 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.1.3-4
- Removed the default SAS link

* Tue Aug 21 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.1.3-3
- Updated with all applicable post-SP4 hotfixes

* Wed Jul 25 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.1.3-2
- Made it a multiple-package spec file, for both the base SAS install and a limited SAS desktop link file

* Fri Jul 08 2005 Andrey Balyakin <aab24@cornell.edu>
- sas9 -> sas91 -> sas913 -> /opt/SAS_9.1.3_OR/sas call chain is created in /usr/local/bin 
