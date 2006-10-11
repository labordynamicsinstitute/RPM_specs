Name: bibtex-harvard
License: GPL
Group: Productivity/Publishing/TeX/Base
Summary: harvard family of bibliographic styles
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 19950416
Release: 0 
URL: http://www.tug.org/ftp/tex-archive/macros/latex/contrib/harvard/ 
Source0: harvard.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch

%description
harvard family of bibliographic styles


%prep

#%setup
tar xzvf %{SOURCE0}
#mv harvard %{name}-%{version}-build 

%build


%install
install -d -m 755 %buildroot/usr/share/texmf/bibtex/bst
cp -a harvard %buildroot/usr/share/texmf/bibtex/bst/

%post
/usr/bin/mktexlsr

%postun
/usr/bin/mktexlsr

%clean
rm -rf %buildroot

%files
/usr/share/texmf/bibtex/bst/harvard/agsm.bst
/usr/share/texmf/bibtex/bst/harvard/apsr.bst
/usr/share/texmf/bibtex/bst/harvard/chicagoa.bst
/usr/share/texmf/bibtex/bst/harvard/dcu.bst
/usr/share/texmf/bibtex/bst/harvard/jmr.bst
/usr/share/texmf/bibtex/bst/harvard/jphysicsB.bst
/usr/share/texmf/bibtex/bst/harvard/kluwer.bst
/usr/share/texmf/bibtex/bst/harvard/nederlands.bst


%changelog
* Wed Oct 11 2006 Lars Vilhuber <lars.vilhuber@cornell.edu> - 19950416-0
- Initial package
 



