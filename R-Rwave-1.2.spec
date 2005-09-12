########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library Rwave
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      1.2
%define packrel  0
%define rel      1
%define packname Rwave
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}.tar.gz
Copyright: Free of charge for non-commercial use.
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Time-Frequency analysis of 1-D signals
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
Rwave is a library of R functions which provide an
environment for the Time-Frequency analysis of 1-D signals (and
especially for the wavelet and Gabor transforms of noisy signals).
It was originally written for Splus by Rene Carmona, Bruno Torresani,
and Wen L. Hwang, first at the University of California at Irvine and
then at Princeton University. Credit should also be given to Andrea
Wang whose functions on the dyadic wavelet transform are included.
Rwave is based on the book:
"PRACTICAL TIME-FREQUENCY ANALYSIS: Gabor and Wavelet Transforms with
an Implementation in S", by Rene Carmona, Wen L. Hwang and Bruno
Torresani, Academic Press (1998).

Author(s)
S original by Rene Carmona <rcarmona@princeton.edu>,
R port by Brandon Whitcher <whitcher@ucar.edu>

08-May-02

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
