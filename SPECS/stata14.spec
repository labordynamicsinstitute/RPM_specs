%define updatever 20150803
# maintenance of stata:
# on an installed system, run 'update all'
# then tar czf /usr/src/redhat/SOURCES/stata14-linux-$updatevar.tgz /usr/local/stata14

Name: stata14
License: Commercial
Group: Application/Statistics
Summary: Stata 14 (standard) from Stata.com 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 14.0 
Release: %{updatever} 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Source0: stata14-linux-%{updatever}.tgz 
Source1: stata14-desktop.tgz

%description
Installs Stata 14 base files. You will need one of -std, -se, and/or -mp,
depending on your license.

You still need to install the license. You can install the license (as root) by 

cd /usr/local/stata14
./stinit

%package java
Group: Application/Statistics
Summary: Common files for Stata: bundled java 
Requires: stata14 >= 14.0
%description java
Common binaries for Stata: bundled Java

%package std
Group: Application/Statistics
Summary: Standard version of Stata 
Requires: stata14 >= 14.0
Requires: stata14-java >= 14.0
%description std
Standard binaries for Stata.

%package se
Group: Application/Statistics
Summary: SE version of Stata 
Requires: stata14 >= 14.0
Requires: stata14-java >= 14.0
%description se
SE binaries for Stata.

%package mp
Group: Application/Statistics
Summary: MP version of Stata 
Requires: stata14 >= 14.0
Requires: stata14-java >= 14.0
%description mp
MP binaries for Stata.

%package sm
Group: Application/Statistics
Summary: Small version of Stata 
Requires: stata14 >= 14.0
Requires: stata14-java >= 14.0
%description sm
Small Stata binaries.

%package desktop
Group: Application/Statistics
Summary: Desktop integration for Stata 
Requires: stata14 >= 14.0
%description desktop
Creates links and desktop icons for Stata 14

%package mkdefault
Group: Application/Statistics
Summary: Make Stata 14 the default
Requires: stata14 >= 14.0

%description mkdefault
Creates links for Stata 14

%prep

%build

%install
# install the desktop files
tar xzf %{SOURCE1}
# install the desktop stuff 
install -d %buildroot/usr/share/applications
install Stata14.desktop %buildroot/usr/share/applications
install Stata14-SE.desktop %buildroot/usr/share/applications
install Stata14-MP.desktop %buildroot/usr/share/applications

# install the core files
cd %buildroot
install -d %buildroot/usr/local/bin
tar xzf %{SOURCE0}  
[[ -f usr/local/stata14/stata.lic ]] && \rm -f usr/local/stata14/stata.lic
ln -sf ../stata14/stata %buildroot/usr/local/bin/stata14
ln -sf ../stata14/xstata %buildroot/usr/local/bin/xstata14
ln -sf ../stata14/stata-se %buildroot/usr/local/bin/stata14-se
ln -sf ../stata14/xstata-se %buildroot/usr/local/bin/xstata14-se
ln -sf ../stata14/stata-mp %buildroot/usr/local/bin/stata14-mp
ln -sf ../stata14/xstata-mp %buildroot/usr/local/bin/xstata14-mp
ln -sf ../stata14/stata-sm %buildroot/usr/local/bin/stata14-sm
ln -sf ../stata14/xstata-sm %buildroot/usr/local/bin/xstata14-sm

# install the default stuff 
cd %buildroot/usr/local/bin
ln -sf stata14 stata
ln -sf stata14-se stata-se
ln -sf stata14-mp stata-mp
ln -sf stata14-sm stata-sm
ln -sf xstata14 xstata
ln -sf xstata14-se xstata-se
ln -sf xstata14-mp xstata-mp
ln -sf xstata14-sm xstata-sm

# add configuration
cd %buildroot/usr/local/stata14
echo "Welcome to the ECCO!" > stata.msg
echo "set processors 1" > profile.do


#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun
if [ "$1" = "0" ]; then
	rm -rf /usr/local/stata14
fi

%clean
#rm -rf %buildroot/usr/local/stata14

%changelog
* Mon Sep 23 2014 Lars Vilhuber <lars.vilhuber@cornell.edu> - 14.0-2
- Updated spec file to Stata 14

%files
%defattr(0755,root,root,0755)
/usr/local/stata14/ado/
/usr/local/stata14/docs/
/usr/local/stata14/auto.dta
/usr/local/stata14/isstata.140
/usr/local/stata14/installed.140
/usr/local/stata14/stinit
/usr/local/stata14/stata_br
/usr/local/stata14/stata_pdf
%attr(770,root,root) /usr/local/stata14/inst2
%attr(770,root,root) /usr/local/stata14/setrwxp
/usr/local/stata14/utilities/update
/usr/local/stata14/utilities/icudt54l.dat

%config
/usr/local/stata14/stata.msg
/usr/local/stata14/profile.do

%files java
/usr/local/stata14/utilities/java

%files std
%defattr(0755,root,root,0755)
/usr/local/bin/stata14
/usr/local/bin/xstata14
/usr/local/stata14/stata
/usr/local/stata14/xstata

%files se
%defattr(0755,root,root,0755)
/usr/local/bin/stata14-se
/usr/local/bin/xstata14-se
/usr/local/stata14/stata-se
/usr/local/stata14/xstata-se

%files sm
%defattr(0755,root,root,0755)
/usr/local/bin/stata14-sm
/usr/local/bin/xstata14-sm
/usr/local/stata14/stata-sm
/usr/local/stata14/xstata-sm

%files mp
%defattr(0755,root,root,0755)
/usr/local/stata14/stata-mp
/usr/local/stata14/xstata-mp
/usr/local/bin/stata14-mp
/usr/local/bin/xstata14-mp

%files desktop
%defattr(0755,root,root,0755)
/usr/share/applications/Stata14.desktop
/usr/share/applications/Stata14-MP.desktop
/usr/share/applications/Stata14-SE.desktop
/usr/local/stata14/stata14.png

%files mkdefault
%defattr(755,root,root)
/usr/local/bin/stata
/usr/local/bin/stata-se
/usr/local/bin/stata-mp
/usr/local/bin/stata-sm
/usr/local/bin/xstata
/usr/local/bin/xstata-se
/usr/local/bin/xstata-sm
/usr/local/bin/xstata-mp

