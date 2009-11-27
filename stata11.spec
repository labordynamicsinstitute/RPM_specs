Name: stata11
License: Commercial
Group: Application/Statistics
Summary: Stata 11 (standard) from Stata.com 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 11.0 
Release: 2 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Source0: stata11-%{_arch}.tgz 
Source1: stata11-desktop.tgz

%description
Installs Stata 11 base files. You will need one of -std, -se, and/or -mp,
depending on your license.

You still need to install the license. You can install the license (as root) by 

cd /usr/local/stata11
./stinit

%package std
Group: Application/Statistics
Summary: Standard version of Stata 
Requires: stata11 >= 11.0
%description std
Standard binaries for Stata.

%package se
Group: Application/Statistics
Summary: SE version of Stata 
Requires: stata11 >= 11.0
%description se
SE binaries for Stata.

%package mp
Group: Application/Statistics
Summary: MP version of Stata 
Requires: stata11 >= 11.0
%description mp
MP binaries for Stata.

%package desktop
Group: Application/Statistics
Summary: Desktop integration for Stata 
Requires: stata11 >= 11.0
%description desktop
Creates links and desktop icons for Stata 11

%package mkdefault
Group: Application/Statistics
Summary: Make Stata 11 the default
Requires: stata11 >= 11.0

%description mkdefault
Creates links for Stata 11

%prep

%build

%install
# install the desktop files
tar xzf %{SOURCE1}
# install the desktop stuff 
install -d %buildroot/opt/kde3/share/applications
install Stata11.desktop %buildroot/opt/kde3/share/applications
install Stata11-SE.desktop %buildroot/opt/kde3/share/applications
install Stata11-MP.desktop %buildroot/opt/kde3/share/applications

# install the core files
cd %buildroot
install -d %buildroot/usr/local/bin
tar xzvf %{SOURCE0}  
[[ -f usr/local/stata11/stata.lic ]] && \rm -f usr/local/stata11/stata.lic
ln -sf ../stata11/stata %buildroot/usr/local/bin/stata11
ln -sf ../stata11/xstata %buildroot/usr/local/bin/xstata11
ln -sf ../stata11/stata-se %buildroot/usr/local/bin/stata11-se
ln -sf ../stata11/xstata-se %buildroot/usr/local/bin/xstata11-se
ln -sf ../stata11/stata-mp %buildroot/usr/local/bin/stata11-mp
ln -sf ../stata11/xstata-mp %buildroot/usr/local/bin/xstata11-mp

# install the default stuff 
cd %buildroot/usr/local/bin
ln -sf stata11 stata
ln -sf stata11-se stata-se
ln -sf stata11-mp stata-mp
ln -sf xstata11 xstata
ln -sf xstata11-se xstata-se
ln -sf xstata11-mp xstata-mp

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun
if [ "$1" = "0" ]; then
	rm -rf /usr/local/stata11
fi

%clean
#rm -rf %buildroot/usr/local/stata11

%changelog

* Thu Aug 30 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.0-1
- Updated spec file to Stata 11

%files
%defattr(0755,root,root,0755)
/usr/local/stata11/ado/
/usr/local/stata11/auto.dta
/usr/local/stata11/isstata.110
/usr/local/stata11/installed.110
/usr/local/stata11/stinit
/usr/local/stata11/stata_br
/usr/local/stata11/stata_pdf
/usr/local/stata11/utilities
%attr(770,root,root) /usr/local/stata11/inst2
%attr(770,root,root) /usr/local/stata11/setrwxp

%config
/usr/local/stata11/stata.msg


%files std
%defattr(0755,root,root,0755)
/usr/local/bin/stata11
/usr/local/bin/xstata11
/usr/local/stata11/stata
/usr/local/stata11/xstata

%files se
%defattr(0755,root,root,0755)
/usr/local/bin/stata11-se
/usr/local/bin/xstata11-se
/usr/local/stata11/stata-se
/usr/local/stata11/xstata-se

%files mp
%defattr(0755,root,root,0755)
/usr/local/stata11/stata-mp
/usr/local/stata11/xstata-mp
/usr/local/bin/stata11-mp
/usr/local/bin/xstata11-mp

%files desktop
%defattr(0755,root,root,0755)
/opt/kde3/share/applications/Stata11.desktop
/opt/kde3/share/applications/Stata11-MP.desktop
/opt/kde3/share/applications/Stata11-SE.desktop
/usr/local/stata11/stata11.png

%files mkdefault
%defattr(755,root,root)
/usr/local/bin/stata
/usr/local/bin/stata-se
/usr/local/bin/stata-mp
/usr/local/bin/xstata
/usr/local/bin/xstata-se
/usr/local/bin/xstata-mp
