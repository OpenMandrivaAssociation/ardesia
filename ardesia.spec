Name:		ardesia
Summary:	A free digital sketchpad software
Version:	1.0 
Release:	%mkrel 2
Source0:	http://ardesia.googlecode.com/files/%{name}-%{version}.tar.bz2
URL:		http://code.google.com/p/ardesia/

Group:		Education
License:	GPLv3 

BuildRequires:	libgsf-devel
BuildRequires:	libsigsegv-devel 
BuildRequires:	vlc-devel
BuildRequires:	binutils-devel
BuildRequires:	gsl-devel
BuildRequires:	libgtk+2.0-devel
BuildRequires:	intltool
BuildRequires:	desktop-file-utils

Requires:	vlc
Requires:	curtain
Requires:	spotlighter
Requires:	desktop-file-utils

%description
Ardesia is the free digital sketchpad software that help you to make colored 
free-hand annotations with digital ink everywhere, record them and share on 
the network. 

%prep 
%setup -q 

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std XDG_UTILS=""

%find_lang %{name}

desktop-file-install	--vendor="" \
			--dir $RPM_BUILD_ROOT%{_datadir}/applications \
			--remove-category="GNOME" \
			--remove-category="GTK" \
			--remove-category="Utility" \
			--add-category="Education" \
			%{buildroot}%{_datadir}/applications/%name.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root,-)
%doc AUTHORS README COPYING NEWS 
%{_bindir}/%name
%{_datadir}/applications/%name.desktop
%{_datadir}/%{name}/ui/*.glade
%{_datadir}/%{name}/scripts/*.sh
%{_datadir}/%{name}/ui/icons/*
%{_datadir}/%{name}/ui/backgrounds/*
%{_datadir}/%{name}/ui/*.xml
%{_datadir}/icons/%name.png
%{_mandir}/man1/%name.*
