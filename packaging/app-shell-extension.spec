
Name: app-shell-extension
Epoch: 1
Version: 2.1.6
Release: 1%{dist}
Summary: Login Shell Extension - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-shell-extension-%{version}.tar.gz
Buildarch: noarch

%description
The Login Shell Extension app provides tools to manage SSH/shell access on the system.

%package core
Summary: Login Shell Extension - Core
Requires: app-base-core
Requires: app-openldap-directory-core
Requires: app-users

%description core
The Login Shell Extension app provides tools to manage SSH/shell access on the system.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/shell_extension
cp -r * %{buildroot}/usr/clearos/apps/shell_extension/

install -D -m 0644 packaging/shell.php %{buildroot}/var/clearos/openldap_directory/extensions/10_shell.php

%post core
logger -p local6.notice -t installer 'app-shell-extension-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/shell_extension/deploy/install ] && /usr/clearos/apps/shell_extension/deploy/install
fi

[ -x /usr/clearos/apps/shell_extension/deploy/upgrade ] && /usr/clearos/apps/shell_extension/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-shell-extension-core - uninstalling'
    [ -x /usr/clearos/apps/shell_extension/deploy/uninstall ] && /usr/clearos/apps/shell_extension/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/shell_extension/packaging
%dir /usr/clearos/apps/shell_extension
/usr/clearos/apps/shell_extension/deploy
/usr/clearos/apps/shell_extension/language
/usr/clearos/apps/shell_extension/libraries
/var/clearos/openldap_directory/extensions/10_shell.php
