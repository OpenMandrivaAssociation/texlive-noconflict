Name:		texlive-noconflict
Version:	30140
Release:	2
Summary:	Resolve macro name conflict between packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/noconflict
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noconflict.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/noconflict.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
