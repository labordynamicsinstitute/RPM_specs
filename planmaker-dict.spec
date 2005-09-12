Name: planmaker-dict
License: Commercial
Group: Application/Office
Summary: Dictionaries for Planmaker spreadsheet
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2004
Release: 1
Requires: planmaker = 2004
Source0: pmldict.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386 

%description
Use PlanMaker on the operating system of your choice: PlanMaker offers the same feature set on all platforms. This application is so compact and efficient that it even provides all its features on mobile Pocket PCs and Handheld PCs -  and fits in a few MBytes of RAM!

A license is required for this software. To obtain a trial license, please go to http://www.softmaker.com/english/tmltrialreg_en.htm

%prep

%build

%install
cd %buildroot
mkdir -p -m 755 %buildroot/opt/softmaker
cd %buildroot/opt/softmaker
tar xzvf %{SOURCE0}  

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean
#rm -rf %buildroot/opt/softmaker/planmaker

%files
/opt/softmaker/planmaker/bulgar.hyp
/opt/softmaker/planmaker/croat.hyp
/opt/softmaker/planmaker/czech.hyp
/opt/softmaker/planmaker/danish.hyp
/opt/softmaker/planmaker/dutch.hyp
/opt/softmaker/planmaker/eston.hyp
/opt/softmaker/planmaker/finnish.hyp
/opt/softmaker/planmaker/french.hyp
/opt/softmaker/planmaker/german.hyp
/opt/softmaker/planmaker/greek.hyp
/opt/softmaker/planmaker/hungary.hyp
/opt/softmaker/planmaker/italian.hyp
/opt/softmaker/planmaker/latvian.hyp
/opt/softmaker/planmaker/lisbonpo.hyp
/opt/softmaker/planmaker/lith.hyp
/opt/softmaker/planmaker/ngerman.hyp
/opt/softmaker/planmaker/norway.hyp
/opt/softmaker/planmaker/norwegia.hyp
/opt/softmaker/planmaker/polish.hyp
/opt/softmaker/planmaker/port.hyp
/opt/softmaker/planmaker/roman.hyp
/opt/softmaker/planmaker/russian.hyp
/opt/softmaker/planmaker/serb.hyp
/opt/softmaker/planmaker/slovak.hyp
/opt/softmaker/planmaker/slovene.hyp
/opt/softmaker/planmaker/spanish.hyp
/opt/softmaker/planmaker/swedish.hyp
/opt/softmaker/planmaker/turk.hyp
/opt/softmaker/planmaker/ukeng.hyp
/opt/softmaker/planmaker/ukraine.hyp
/opt/softmaker/planmaker/useng.hyp
/opt/softmaker/planmaker/brazport.dcn
/opt/softmaker/planmaker/canfren.dcn
/opt/softmaker/planmaker/danish.dcn
/opt/softmaker/planmaker/dutch.dcn
/opt/softmaker/planmaker/french.dcn
/opt/softmaker/planmaker/italian.dcn
/opt/softmaker/planmaker/lisbonpo.dcn
/opt/softmaker/planmaker/mexican.dcn
/opt/softmaker/planmaker/norwegia.dcn
/opt/softmaker/planmaker/nswiss.dcn
/opt/softmaker/planmaker/spanish.dcn
/opt/softmaker/planmaker/swedish.dcn
/opt/softmaker/planmaker/swissger.dcn
