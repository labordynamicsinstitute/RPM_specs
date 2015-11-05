%define updatever 20150603
# maintenance of stata:
# on an installed system, run 'update all'
# then tar czf /usr/src/redhat/SOURCES/stata13-linux-$updatevar.tgz /usr/local/stata13

Name: stata13
License: Commercial
Group: Application/Statistics
Summary: Stata 13 (standard) from Stata.com 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 13.1 
Release: %{updatever} 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Source0: stata13-linux-%{updatever}.tgz 
Source1: stata13-desktop.tgz

%description
Installs Stata 13 base files. You will need one of -std, -se, and/or -mp,
depending on your license.

You still need to install the license. You can install the license (as root) by 

cd /usr/local/stata13
./stinit

%package java
Group: Application/Statistics
Summary: Common files for Stata: bundled java 
Requires: stata13 >= 13.0
%description java
Common binaries for Stata: bundled Java

%package std
Group: Application/Statistics
Summary: Standard version of Stata 
Requires: stata13 >= 13.0
Requires: stata13-java >= 13.0
%description std
Standard binaries for Stata.

%package se
Group: Application/Statistics
Summary: SE version of Stata 
Requires: stata13 >= 13.0
Requires: stata13-java >= 13.0
%description se
SE binaries for Stata.

%package mp
Group: Application/Statistics
Summary: MP version of Stata 
Requires: stata13 >= 13.0
Requires: stata13-java >= 13.0
%description mp
MP binaries for Stata.

%package sm
Group: Application/Statistics
Summary: Small version of Stata 
Requires: stata13 >= 13.0
Requires: stata13-java >= 13.0
%description sm
Small Stata binaries.

%package desktop
Group: Application/Statistics
Summary: Desktop integration for Stata 
Requires: stata13 >= 13.0
%description desktop
Creates links and desktop icons for Stata 13

%package mkdefault
Group: Application/Statistics
Summary: Make Stata 13 the default
Requires: stata13 >= 13.0

%description mkdefault
Creates links for Stata 13

%prep

%build

%install
# install the desktop files
tar xzf %{SOURCE1}
# install the desktop stuff 
install -d %buildroot/usr/share/applications
install Stata13.desktop %buildroot/usr/share/applications
install Stata13-SE.desktop %buildroot/usr/share/applications
install Stata13-MP.desktop %buildroot/usr/share/applications

# install the core files
cd %buildroot
install -d %buildroot/usr/local/bin
tar xzf %{SOURCE0}  
[[ -f usr/local/stata13/stata.lic ]] && \rm -f usr/local/stata13/stata.lic
ln -sf ../stata13/stata %buildroot/usr/local/bin/stata13
ln -sf ../stata13/xstata %buildroot/usr/local/bin/xstata13
ln -sf ../stata13/stata-se %buildroot/usr/local/bin/stata13-se
ln -sf ../stata13/xstata-se %buildroot/usr/local/bin/xstata13-se
ln -sf ../stata13/stata-mp %buildroot/usr/local/bin/stata13-mp
ln -sf ../stata13/xstata-mp %buildroot/usr/local/bin/xstata13-mp
ln -sf ../stata13/stata-sm %buildroot/usr/local/bin/stata13-sm
ln -sf ../stata13/xstata-sm %buildroot/usr/local/bin/xstata13-sm

# install the default stuff 
cd %buildroot/usr/local/bin
ln -sf stata13 stata
ln -sf stata13-se stata-se
ln -sf stata13-mp stata-mp
ln -sf stata13-sm stata-sm
ln -sf xstata13 xstata
ln -sf xstata13-se xstata-se
ln -sf xstata13-mp xstata-mp
ln -sf xstata13-sm xstata-sm

# add configuration
cd %buildroot/usr/local/stata13
echo "Welcome to the ECCO!" > stata.msg
echo "set processors 1" > profile.do


#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun
if [ "$1" = "0" ]; then
	rm -rf /usr/local/stata13
fi

%clean
#rm -rf %buildroot/usr/local/stata13

%changelog
* Mon Sep 23 2013 Lars Vilhuber <lars.vilhuber@cornell.edu> - 13.0-2
- Updated spec file to Stata 13

%files
%defattr(0755,root,root,0755)
/usr/local/stata13/ado/
/usr/local/stata13/docs/
/usr/local/stata13/auto.dta
/usr/local/stata13/isstata.130
/usr/local/stata13/installed.130
/usr/local/stata13/stinit
/usr/local/stata13/stata_br
/usr/local/stata13/stata_pdf
%attr(770,root,root) /usr/local/stata13/inst2
%attr(770,root,root) /usr/local/stata13/setrwxp
/usr/local/stata13/utilities/update

%config
/usr/local/stata13/stata.msg
/usr/local/stata13/profile.do

%files java
/usr/local/stata13/utilities/java

%files std
%defattr(0755,root,root,0755)
/usr/local/bin/stata13
/usr/local/bin/xstata13
/usr/local/stata13/stata
/usr/local/stata13/xstata

%files se
%defattr(0755,root,root,0755)
/usr/local/bin/stata13-se
/usr/local/bin/xstata13-se
/usr/local/stata13/stata-se
/usr/local/stata13/xstata-se

%files sm
%defattr(0755,root,root,0755)
/usr/local/bin/stata13-sm
/usr/local/bin/xstata13-sm
/usr/local/stata13/stata-sm
/usr/local/stata13/xstata-sm

%files mp
%defattr(0755,root,root,0755)
/usr/local/stata13/stata-mp
/usr/local/stata13/xstata-mp
/usr/local/bin/stata13-mp
/usr/local/bin/xstata13-mp

%files desktop
%defattr(0755,root,root,0755)
/usr/share/applications/Stata13.desktop
/usr/share/applications/Stata13-MP.desktop
/usr/share/applications/Stata13-SE.desktop
/usr/local/stata13/stata13.png

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

