# revision 30140
# category Package
# catalog-ctan /macros/latex/contrib/noconflict
# catalog-date 2013-04-27 00:34:43 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-noconflict
Version:	1.0
Release:	2
Summary:	Resolve macro name conflict between packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/noconflict
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noconflict.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noconflict.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides several commands to prefix (and hence
obscure) a macro's (or a sequence of macros') name, and to
restore the original macro(s) at places in a document where
they are needed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/noconflict/noconflict.sty
%doc %{_texmfdistdir}/doc/latex/noconflict/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
