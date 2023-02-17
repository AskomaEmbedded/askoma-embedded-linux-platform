ASKOMA_VALID_MACHINES = []

def __set_defaults_askoma():

    import os
    import sys

    # Append to valid machines
    global ASKOMA_VALID_MACHINES
    ASKOMA_VALID_MACHINES += [
        'imx6ull-em-r1',
        'imx8mm-em-r1',
    ]

    local_conf_exists = os.path.isfile(os.path.join(build_dir,
                                                    'conf',
                                                    'local.conf'))

    def required_var_error(varname, valid_vals):
        sys.stderr.write("ERROR: You must set '%s' before setting up the environment.\n" %
                         (varname,))
        sys.stderr.write("       Set MACHINE variable with one of the possible values.\n"
                         "       Possible values are: %s\n\n"
                         "       Ex: MACHINE=imx6ull-em-r1 source setup-environment build\n"
                         % valid_vals)
        sys.exit(1)

    def maybe_set_default(varname, valid_vals):
        try:
            val = os.environ[varname]
        except KeyError:
            val = None

        if val:
            if val in valid_vals:
                set_default(varname, val)
            else:
                required_var_error(varname, valid_vals)
        elif not local_conf_exists:
            required_var_error(varname, valid_vals)

    maybe_set_default('MACHINE', ASKOMA_VALID_MACHINES)
    set_default('DISTRO', 'oel')
    set_default('SDKMACHINE', 'x86_64')

run_set_defaults(__set_defaults_askoma)