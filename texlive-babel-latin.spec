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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The babel-latin package provides the babel languages latin,
classicallatin, medievallatin, and ecclesiasticallatin. It also defines
several useful shorthands as well as some modifiers for typographical
fine-tuning.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-latin
%dir %{_datadir}/texmf-dist/source/generic/babel-latin
%dir %{_datadir}/texmf-dist/tex/generic/babel-latin
%doc %{_datadir}/texmf-dist/doc/generic/babel-latin/README
%doc %{_datadir}/texmf-dist/doc/generic/babel-latin/latin.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-latin/latin.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-latin/latin.ins
%{_datadir}/texmf-dist/tex/generic/babel-latin/classicallatin.ldf
%{_datadir}/texmf-dist/tex/generic/babel-latin/classiclatin.ldf
%{_datadir}/texmf-dist/tex/generic/babel-latin/ecclesiasticallatin.ldf
%{_datadir}/texmf-dist/tex/generic/babel-latin/ecclesiasticallatin.lua
%{_datadir}/texmf-dist/tex/generic/babel-latin/ecclesiasticlatin.ldf
%{_datadir}/texmf-dist/tex/generic/babel-latin/latin.ldf
%{_datadir}/texmf-dist/tex/generic/babel-latin/medievallatin.ldf
