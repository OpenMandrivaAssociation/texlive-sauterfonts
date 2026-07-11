%global tl_name sauterfonts
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Use Sauters fonts in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sauterfonts
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sauterfonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sauterfonts.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sauterfonts.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides font definition files (plus a replacement for the
package exscale) to access many of the fonts in Sauter's collection.
These fonts are available in all point sizes and look nicer for such
"intermediate" document sizes as 11pt. Also included is the package
sbbm, an alternative to access the bbm fonts.

