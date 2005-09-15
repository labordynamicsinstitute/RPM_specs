# based on a spec file generated by build-R-contrib-rpms.pl #################
# spec file for R view economics
#
# Lars Vilhuber (lars.vilhuber@cornell.edu) 
#
%define ver      1.0
%define packrel  2.1.1
%define rel      1.vrdc
%define viewname view-bayesian
%define prefix   /usr
%define library  %{prefix}/lib/R/library

Name: R-%{viewname}
Version: %{ver}.R%{packrel}
Release: %{rel}
Source: %{name}_%{ver}.tgz
Copyright: LGPL
URL: http://cran.r-project.org/src/contrib/Views/Bayesian.html
Group: Applications/Math
Summary: R view %{viewname} - Bayesian Inference
BuildRequires: R-base
PreReq: R-base R-view-core-bayesian-econ
BuildRoot: /var/tmp/%{viewname}-buildroot

%description
R %{viewname}:
Maintainer: Jong Hee Park

Applied researchers interested in Bayesian statistics are increasingly attracted to R because of the ease of which one can code algorithms to sample from posterior distributions as well as the significant number of packages contributed to the Comprehensive R Archive Network (CRAN) that provide tools for Bayesian inference. This task view catalogs these tools. In this task view, we divide those packages into four groups based on the scope and focus of the packages. We first review R packages that provide Bayesian estimation tools for a wide range of models. We then discuss packages that address specific Bayesian models or specialized methods in Bayesian statistics. This is followed by a description of packages used for post-estimation analysis. Finally, we review packages that link R to other Bayesian sampling engines such as JAGS , OpenBUGS , and WinBUGS .

This is a preliminary task view, and we have likely missed some important information. Please email the task view maintainer with any feedback.

    * Bayesian packages for general model fitting: bayesm provides R functions for Bayesian inference for various models widely used in marketing and micro-econometrics. The models include linear regression models, multinomial logit, multinomial probit, multivariate probit, multivariate mixture of normals, hierarchical linear models, and linear instrumental variable models. bayesSurv contains R functions to perform Bayesian inference for various survival regression models. MCMCpack provides model-specific Markov chain Monte Carlo (MCMC) algorithms for wide range of models commonly used in the social and behavioral sciences. It contains R functions to fit a number a regression models (linear regression, logit, ordinal probit, probit, Poisson regression, etc.), measurement models (item response theory and factor models), and models for ecological inference. It also contains a generic Metropolis sampler that can be used to fit arbitrary models. All MCMCpack functions return mcmc objects that can be analyzed with methods defined in the coda package. The package mcmc consists of an R function for a random-walk Metropolis algorithm for a continuous random vector.
    * Bayesian packages for specific models or methods : The baymvb package fits multivariate binary regression models (multivariate probit or multivariate t-link models) using posterior simulation. bqtl can be used to fit quantitative trait loci (QTL) models. This package allows Bayesian estimation of multi-gene models via Laplace approximations and provides tools for interval mapping of genetic loci. bim provides a function for Bayesian interval mapping using MCMC methods. Both of these packages contain graphical tools for QTL analysis. The BMA package has functions for Bayesian model averaging for linear models, generalized linear models, and survival models. The complementary package ensembleBMA uses the BMA package to create probabilistic forecasts of ensembles using a mixture of normal distributions. deal provides R functions for Bayesian network analysis; the current version of covers discrete and continuous variables under Gaussian network structure. EbayesThresh implements Bayesian estimation for thresholding methods. Although the original model is developed in the context of wavelets, this package is useful when researchers need to take advantage of possible sparsity in a parameter set. eco fits Bayesian ecological inference models in two by two tables using MCMC methods. evdbayes provides tools for Bayesian analysis of extreme value models. exactLoglinTest provides functions for log-linear models that compute Monte Carlo estimates of conditional P-values for goodness of fit tests. The gbayes() function in Hmisc derives the posterior (and optionally) the predictive distribution when both the prior and the likelihood are Gaussian, and when the statistic of interest comes from a two-sample problem. The function krige.bayes() in the geoR package performs Bayesian analysis of geostatistical data allowing specification of different levels of uncertainty in the model parameters. The binom.krige.bayes() function in the geoRglm package implements Bayesian posterior simulation and spatial prediction for the binomial spatial model (see the Spatial view for more information). The mcmcsamp() function in lme4 allows MCMC sampling for the linear mixed model and generalized linear mixed model. The MNP package fits multinomial probit models using MCMC methods. sna, an R package for social network analysis, contains functions to generate posterior samples from Butt's Bayesian network accuracy model using Gibbs sampling. The vcov.gam() function the mgcv package can extract a Bayesian posterior covariance matrix of the parameters from a fitted gam object. vabayelMix provides R functions to perform Bayesian inference for a Gaussian mixture model using a variational approach.
    * Post-estimation tools : The boa package provides functions for diagnostics, summarization, and visualization of MCMC sequences. It imports draws from BUGS format, or from plain matrices. boa provides the Gelman and Rubin, Geweke, Heidelberger and Welch, and Raftery and Lewis diagnostics, the Brooks and Gelman multivariate shrink factors. The coda (Convergence Diagnosis and Output Analysis) package is a suite of functions that can be used to summarize, plot, and and diagnose convergence from MCMC samples. coda also defines an mcmc object and related methods which are used by other packages. It can easily import MCMC output from WinBUGS, OpenBUGS, and JAGS, or from plain matrices. coda contains the Gelman and Rubin, Geweke, Heidelberger and Welch, and Raftery and Lewis diagnostics. mcgibbsit provides the Warnes and Raftery MCGibbsit MCMC diagnostic. It operates on mcmc objects.
    * Packages that link R to other sampling engines : bayesmix is an R package to fit Bayesian mixture models using JAGS . BRugs provides an R interface on Windows machines to OpenBUGS . There are two packages that can be used to interface R with WinBUGS . R2WinBUGS provides a set of functions to call WinBUGS on a Windows system; rbugs supports Linux systems by running WinBUGS through WINE . All of these BUGS engines use graphical models for model specification. As such, the gR task view may be of interest.

The Bayesian Inference Task View is written by Jong Hee Park and Andrew D. Martin (Washington University, St. Louis, MO, USA), and Kevin M. Quinn (Harvard University, Cambridge, MA, USA). Please email the task view maintainer jhpark@artsci.wustl.edu with suggestions.



#%define _unpackaged_files_terminate_build 0
#%define _missing_doc_files_terminate_build 0

%prep
%setup -T -c -a 0

%build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{library}
#install -p -d -D *  $RPM_BUILD_ROOT%{library}
mv *  $RPM_BUILD_ROOT%{library}/
chmod -R a+rX  $RPM_BUILD_ROOT%{library}
chown -R root.root  $RPM_BUILD_ROOT%{library}
# create DESCRIPTION
wget %{url}
echo "On SLES9, the WinBugs packages have been removed." > README.sles9
%clean
rm -rf $RPM_BUILD_ROOT

%post
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{library}/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%postun
%{prefix}/bin/R CMD perl %{prefix}/lib/R/share/perl/build-help.pl --htmllists
cat %{library}/*/CONTENTS > %{prefix}/lib/R/doc/html/search/index.txt

%files
%doc Bayesian.html README.sles9
%{library}/bayesmix
%{library}/bayesSurv
%{library}/baymvb
%{library}/bim
%{library}/BMA
%{library}/boa
%{library}/bqtl
%{library}/deal
%{library}/dynamicGraph
%{library}/EbayesThresh
%{library}/ensembleBMA
%{library}/evdbayes
%{library}/exactLoglinTest
%{library}/geoR
%{library}/geoRglm
%{library}/mcgibbsit
%{library}/mcmc
%{library}/MCMCpack
%{library}/sna
%{library}/vabayelMix



####### end of spec-file ################################################
