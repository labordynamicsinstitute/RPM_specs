########## automatically generated by build-R-contrib-rpms.pl #################
# spec file for R library haplo.score
#
# D. Steuer <detlef.steuer@gmx.de>
#
%define ver      1.0.2
%define packrel  0
%define rel      1
%define packname haplo.score
%define prefix   /usr

Name: R-%{packname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{ver}.tar.gz
Copyright: Copyright 2001 Mayo Foundation for Medical Educationand Research..This program is free software; you can redistribute it and/ormodify it under the terms of the GNU General Public Licenseas published by the Free Software Foundation; either version 2of the License, or (at your option) any later version..This program is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY; without even the implied warranty ofMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See theGNU General Public License for more details..You should have received a copy of the GNU General Public Licensealong with this program; if not, write to the Free SoftwareFoundation, Inc., 59 Temple Place - Suite 330, Boston, MA02111-1307, USA..
URL: http://cran.r-project.org/contrib
Group: Applications/Math
Summary: R package %{packname} - Score Tests for Association of Traits with Haplotypes when Linkage Phase is Ambiguous.
BuildRequires: R-base
PreReq: R-base
BuildRoot: /var/tmp/%{packname}-buildroot

%description
R package:
A suite of routines that can be used to compute score
statistics to test associations between haplotypes and a wide
variety of traits, including binary, ordinal, quantitative, and
Poisson. These methods assume that all subjects are unrelated and
that haplotypes are ambiguous (due to unknown linkage phase of the
genetic markers). The methods provide several different global and
haplotype-specific tests for association, as well as provide
adjustment for non-genetic covariates and computation of simulation
p-values (which may be needed for sparse data). Details on the
background and theory of the score statistics can be found in the
following reference:
.
Schaid DJ, Rowland CM, Tines DE, Jacobson RM, Poland GA.
Score tests for association of traits with haplotypes when
linkage phase is ambiguous. American J Human Genetics, February,
2002.

Author(s)
Charles M. Rowland, David E. Tines, and Daniel J. Schaid
<schaid@mayo.edu>.  R version translation by Gregory R. Warnes
<gregory_r_warnes@groton.pfizer.com>

2002-09-13

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
