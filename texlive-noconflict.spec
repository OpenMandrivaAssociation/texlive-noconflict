%global tl_name noconflict
%global tl_revision 30140

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Resolve macro name conflict between packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/noconflict
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noconflict.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/noconflict.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides several commands to prefix (and hence obscure) a
macro's (or a sequence of macros') name, and to restore the original
macro(s) at places in a document where they are needed.

