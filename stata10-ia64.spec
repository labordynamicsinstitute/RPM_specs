Name: stata10
License: Commercial
Group: Application/Statistics
Summary: Stata 10 (standard) from Stata.com 
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 10.0 
Release: 2 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Source0: stata10-ia64.tgz 
Source1: stata10-desktop.tgz

%description
Installs Stata 10 base files. You will need one of -std, -se, and/or -mp,
depending on your license.

You still need to install the license. You can install the license (as root) by 

cd /usr/local/stata10
./stinit

%package std
Group: Application/Statistics
Summary: Standard version of Stata 
Requires: stata10 >= 10.0
%description std
Standard binaries for Stata.

%package se
Group: Application/Statistics
Summary: SE version of Stata 
Requires: stata10 >= 10.0
%description se
SE binaries for Stata.

%package desktop
Group: Application/Statistics
Summary: Stata 10 desktop integration
Requires: stata10 >= 10.0
%description desktop
Creates links and desktop icons for Stata 10

%prep

%build

%install
cd %buildroot
mkdir -p -m 755 %buildroot/usr/local/bin
tar xzvf %{SOURCE0}  
tar xzf %{SOURCE1}

ln -s ../stata10/stata %buildroot/usr/local/bin/stata10
ln -s ../stata10/xstata %buildroot/usr/local/bin/xstata10
ln -s ../stata10/stata-se %buildroot/usr/local/bin/stata10-se
ln -s ../stata10/xstata-se %buildroot/usr/local/bin/xstata10-se
# install the desktop stuff 
install -d %buildroot/opt/kde3/share/applications
install Stata10.desktop %buildroot/opt/kde3/share/applications
install Stata10-SE.desktop %buildroot/opt/kde3/share/applications
install Stata10-MP.desktop %buildroot/opt/kde3/share/applications
rm -f *desktop

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun
if [ "$1" = "0" ]; then
	rm -rf /usr/local/stata10
fi

%clean
#rm -rf %buildroot/usr/local/stata10

%changelog
* Fri Sep 25 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 10.0-2
- Removed MP files (no license here), added desktop entries


* Thu Aug 30 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.0-1
- Updated spec file to Stata 10

%files
%defattr(0755,root,root,0755)
/usr/local/stata10/ado/
/usr/local/stata10/icons/
/usr/local/stata10/auto.dta
/usr/local/stata10/isstata.100
/usr/local/stata10/installed.100
/usr/local/stata10/stinit
/usr/local/stata10/stata_br
%attr(770,root,root) /usr/local/stata10/inst2
%attr(770,root,root) /usr/local/stata10/setrwxp

%config
/usr/local/stata10/stata.msg

%files std
%defattr(0755,root,root,0755)
/usr/local/bin/stata10
/usr/local/bin/xstata10
/usr/local/stata10/stata
/usr/local/stata10/xstata

%files se
%defattr(0755,root,root,0755)
/usr/local/bin/stata10-se
/usr/local/bin/xstata10-se
/usr/local/stata10/stata-se
/usr/local/stata10/xstata-se

%files desktop
%defattr(755,root,root)
/opt/kde3/share/applications/Stata10.desktop
/opt/kde3/share/applications/Stata10-MP.desktop
/opt/kde3/share/applications/Stata10-SE.desktop

