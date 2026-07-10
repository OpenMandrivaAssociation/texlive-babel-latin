%global tl_name babel-latin
%global tl_revision 76176

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.3
Release:	%{tl_revision}.1
Summary:	Babel support for Latin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/latin
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-latin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-latin.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-latin.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The babel-latin package provides the babel languages latin,
classicallatin, medievallatin, and ecclesiasticallatin. It also defines
several useful shorthands as well as some modifiers for typographical
fine-tuning.

