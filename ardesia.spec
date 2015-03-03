%define svn_ver 20141221

Name:           ardesia
Summary:        A free digital sketchpad software
Version:        1.2 
Release:        0.%{svn_ver}.1
Source0:        http://ardesia.googlecode.com/files/%{name}-%{version}-%{svn_ver}.tar.gz
URL:            http://code.google.com/p/ardesia
Group:          Education
License:        GPLv3 


BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  libsigsegv-devel 
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libvlc)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(blas)
BuildRequires:	libatlas-devel
BuildRequires:	libsigsegv-devel 
BuildRequires:	binutils-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	desktop-file-utils


Suggests:    vlc
Suggests:    vlc-plugin-theora 
Suggests:    xdg-utils
Suggests:    curtain
Suggests:    florence

%description
Ardesia is the free digital sketchpad software that help you to make colored 
free-hand annotations with digital ink everywhere, record them and share on 
the network. 

%prep 
%setup -q -n %{name}-%{version}-%{svn_ver}

%build
./autogen.sh
%configure
%make

%install
%makeinstall_std XDG_UTILS=""

%find_lang %{name}

desktop-file-install    --vendor="" \
                        --dir %{buildroot}%{_datadir}/applications \
                        --remove-category="GNOME" \
                        --remove-category="GTK" \
                        --remove-category="Utility" \
                        --add-category="Education" \
                        %{buildroot}%{_datadir}/applications/%name.desktop

%files -f %name.lang
%doc AUTHORS README COPYING NEWS 
%{_bindir}/%name
%{_datadir}/applications/%name.desktop
%{_datadir}/%{name}/ui/*.glade
%{_datadir}/%{name}/scripts/*.sh
%{_datadir}/%{name}/ui/icons/*
%{_datadir}/%{name}/ui/backgrounds/*
%{_datadir}/%{name}/ui/*.xml
%{_datadir}/pixmaps/%name.png
%{_mandir}/man1/%name.*

