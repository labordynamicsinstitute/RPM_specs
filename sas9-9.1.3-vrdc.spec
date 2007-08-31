Name: sas9
License: Commercial
Group: Application/Statistics
Summary: SAS 9.1.3 
Packager: Lars Vilhuber
Version: 9.1.3
Release: 3
Source0: SAS_9.1.3_installed.tgz
Source1: SAS-desktop.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 

%description
Manages installation of SAS. 

%package desktop
Group: Application/Statistics
BuildArch: noarch
Summary: SAS 9.1.3 desktop links
%description desktop
Creates links and desktop icons for SAS.

%prep

%build

%install
# install the base SAS
install -d %buildroot/opt/SAS_9.1.3
install -d %buildroot/usr/local/bin
cd %buildroot
tar xf %{SOURCE0} 
ln -s /opt/SAS_9.1.3/sas %buildroot/usr/local/bin/sas913
ln -s sas913 %buildroot/usr/local/bin/sas91
ln -s sas91 %buildroot/usr/local/bin/sas9
ln -s sas9 %buildroot/usr/local/bin/sas

# install the desktop stuff 
install -d %buildroot/opt/kde3/share/applications
tar xf %{SOURCE1}

%post


%preun

%postun

%clean

%files
%defattr(755,root,root)

%config
/opt/SAS_9.1.3/sasv9_local.cfg

/opt/SAS_9.1.3

%files desktop
%defattr(755,root,root)
/opt/kde3/share/applications/SAS.desktop
/usr/local/bin/sas
/usr/local/bin/sas9
/usr/local/bin/sas91
/usr/local/bin/sas913

%changelog
* Tue Aug 21 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.1.3-3
- Updated with all applicable post-SP4 hotfixes

* Wed Jul 25 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.1.3-2
- Made it a multiple-package spec file, for both the base SAS install and a limited SAS desktop link file

* Fri Jul 08 2005 Andrey Balyakin <aab24@cornell.edu>
- sas9 -> sas91 -> sas913 -> /opt/SAS_9.1.3_OR/sas call chain is created in /usr/local/bin 
