Name: kde-splash-SRD
License: GPL
Group: System/GUI/KDE
Summary: KDE splash theme with SRD warning message
Packager: Mohammed Chaudhry <mohammed.chaudhry@census.gov>
Version: 1
Release: 0
Source0: SRDsplash.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
SRD splash with Warning Message.

%prep

%build

%install
install -d -m 755 %buildroot/opt/kde3/share/apps/ksplash/Themes
cd %buildroot/opt/kde3/share/apps/ksplash/Themes
tar xvf %{SOURCE0}  

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean


%files
/opt/kde3/share/apps/ksplash/Themes/SRDsplash
