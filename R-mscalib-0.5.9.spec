########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library mscalib
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      0.5.9
%define packrel  0
%define rel      1
%define packname mscalib
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}.tar.gz
Copyright: GPL version 2 or newer
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Calibration and filtering of MALDI-TOF Peptide Mass Fingerprint data.
BuildRequires: R-base
PreReq: R-base
Requires:  R-dr
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Calibration and filtering methods for calibration of mass spectrometric peptide mass lists. Includes methods for internal, external calibration of mass lists. Provides methods for filtering chemical noise and peptide contaminants.

Author(s)
Eryk Witold Wolski <wolski@molgen.mpg.de>

2004-01-28

%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0

%prep
%setup -T -c -a 0

%build
cp %{packname}/DESCRIPTION .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{prefix}/lib/R/library
%{prefix}/bin/R CMD INSTALL -l $RPM_BUILD_ROOT%{prefix}/lib/R/library %{packname}
%{prefix}/bin/R CMD check %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)


%clean
rm -rf $RPM_BUILD_ROOT

%post
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%postun
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{prefix}/lib/R/library/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%files
%doc DESCRIPTION
%{prefix}/lib/R/library/%{packname}


####### end of spec-file ################################################
