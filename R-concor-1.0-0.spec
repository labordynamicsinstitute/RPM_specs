########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library concor
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      1.0
%define packrel  0
%define rel      1
%define packname concor
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}-%{packrel}.tar.gz
Copyright: GPL
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Concordance
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
The four functions svdcp (cp for column partitioned), svdbip or
svdbip2 (bip for bi-partitioned), and svdbips (s for a simultaneous
optimization of one set of r solutions), correspond to a "SVD by
blocks" notion, by supposing each block depending on relative
subspaces, rather than on two whole spaces as usual SVD does. The
other functions, based on this notion, are relative to two column
partitioned data matrices x and y defining two sets of subsets xi and
yj of variables and amount to estimate a link between xi and yj for
the pair (xi, yj) relatively to the links associated to all the other
pairs.

Author(s)
R. Lafosse <lafosse@lsp.ups-tlse.fr>

2004-07-09

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
