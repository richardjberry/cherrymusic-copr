Name:           cherrymusic
Version:        0.40.0
Release:        1%{?dist}
Summary:        A standalone HTML5 (with Flash fallback) music streaming server based on CherryPy and jPlayer.

License:        GPLv3
URL:            http://fomori.org/cherrymusic
Source0:        https://github.com/devsnd/cherrymusic/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python3, python3-devel, python3-cherrypy
Requires:       python3, python3-cherrypy

BuildArch:      noarch

%description
# TODO: Write description


%prep
%setup -q


%install
mkdir -p %{buildroot}/%{_bindir}
python3 "setup.py" install --root="%{buildroot}" --optimize=1
mkdir -p %{buildroot}%{_mandir}/man{1,5,8}
install -m644 "doc/man/%{name}.1.gz" "%{buildroot}%{_mandir}/man1"
install -m644 "doc/man/%{name}.conf.5.gz" "%{buildroot}%{_mandir}/man5"
install -m644 "doc/man/%{name}d.8.gz" "%{buildroot}%{_mandir}/man8"


%files
%{_bindir}/%{name}
%{_bindir}/%{name}-tray
%{_bindir}/%{name}d
%{python3_sitelib}/%{name}server/
%{python3_sitelib}/audiotranscode/
%{python3_sitelib}/backport/
%{python3_sitelib}/CherryMusic-%{version}-py3.6.egg-info/
%{python3_sitelib}/cmbootstrap/
%{python3_sitelib}/tinytag/
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man5/%{name}.conf.5.gz
%{_mandir}/man8/%{name}d.8.gz
%license COPYING


%changelog
* Mon Sep 11 2017 Richard Berry <rjsberry@protonmail.com> - 0.40.0-1
- First cherrymusic package
