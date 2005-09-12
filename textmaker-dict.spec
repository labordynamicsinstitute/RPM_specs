Name: textmaker-dict
License: Commercial
Group: Application/Office
Summary: Dictionaries for Textmaker word processor
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2002
Release: 1
Requires: textmaker = 2002
Source0: tmldict.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386 

%description
There is only one word processor that is available for Windows, Linux, FreeBSD, Pocket PCs, Handheld PCs, Windows CE.NET, and now for Sharp Zaurus: TextMaker 2002.

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
#rm -rf %buildroot/opt/softmaker/textmaker

%files
/opt/softmaker/textmaker/brazport.dcn
/opt/softmaker/textmaker/canfren.dcn
/opt/softmaker/textmaker/chconv.thn
/opt/softmaker/textmaker/danish.dcn
/opt/softmaker/textmaker/danish.hyp
/opt/softmaker/textmaker/dutch.dcn
/opt/softmaker/textmaker/dutch.hyp
/opt/softmaker/textmaker/dutch.thn
/opt/softmaker/textmaker/euro.thn
/opt/softmaker/textmaker/french.dcn
/opt/softmaker/textmaker/french.hyp
/opt/softmaker/textmaker/french.thn
/opt/softmaker/textmaker/gerconv.thn
/opt/softmaker/textmaker/italian.dcn
/opt/softmaker/textmaker/italian.hyp
/opt/softmaker/textmaker/italian.thn
/opt/softmaker/textmaker/lisbonpo.dcn
/opt/softmaker/textmaker/lisbonpo.hyp
/opt/softmaker/textmaker/mexican.dcn
/opt/softmaker/textmaker/norwegia.dcn
/opt/softmaker/textmaker/norwegia.hyp
/opt/softmaker/textmaker/nswiss.dcn
/opt/softmaker/textmaker/nswiss.thn
/opt/softmaker/textmaker/spanish.dcn
/opt/softmaker/textmaker/spanish.hyp
/opt/softmaker/textmaker/spanish.thn
/opt/softmaker/textmaker/swedish.dcn
/opt/softmaker/textmaker/swedish.hyp
/opt/softmaker/textmaker/swissger.dcn
/opt/softmaker/textmaker/swissger.thn

