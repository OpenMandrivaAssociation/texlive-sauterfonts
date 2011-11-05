# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sauterfonts
# catalog-date 2007-01-14 10:43:12 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-sauterfonts
Version:	20070114
Release:	1
Summary:	Use sauter fonts in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sauterfonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sauterfonts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sauterfonts.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sauterfonts.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A package providing font definition files (plus a replacement
for the package exscale) to access many of the fonts in
Sauter's collection. These fonts are available in all point
sizes and look nicer for such "intermediate" document sizes as
11pt. Also included is the package sbbm, an alternative to
access the bbm fonts, a nice collection of blackboard bold
symbols.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sauterfonts/sbbm.sty
%{_texmfdistdir}/tex/latex/sauterfonts/sexscale.sty
%{_texmfdistdir}/tex/latex/sauterfonts/somlcmm.fd
%{_texmfdistdir}/tex/latex/sauterfonts/somlcmr.fd
%{_texmfdistdir}/tex/latex/sauterfonts/somscmr.fd
%{_texmfdistdir}/tex/latex/sauterfonts/somscmsy.fd
%{_texmfdistdir}/tex/latex/sauterfonts/somxcmex.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmdh.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmfib.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmfr.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmr.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmss.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmtt.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sot1cmvtt.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbm.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbmdh.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbmfib.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbmss.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbmtt.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbmvtt.fd
%{_texmfdistdir}/tex/latex/sauterfonts/subbold.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sucmr.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sucmss.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sucmtt.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sulasy.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sumsa.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sumsb.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sursfs.fd
%{_texmfdistdir}/tex/latex/sauterfonts/sustmry.fd
%{_texmfdistdir}/tex/latex/sauterfonts/suwasy.fd
%doc %{_texmfdistdir}/doc/latex/sauterfonts/README
#- source
%doc %{_texmfdistdir}/source/latex/sauterfonts/sauterfonts.fdd
%doc %{_texmfdistdir}/source/latex/sauterfonts/sauterfonts.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
