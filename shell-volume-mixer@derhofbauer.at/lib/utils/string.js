/**
 * Shell Volume Mixer
 *
 * String utilities.
 *
 * @author Alexander Hofbauer <alex@derhofbauer.at>
 */

/* exported repeat, versionGreaterOrEqual */


/**
 * Parses a version string and returns an array.
 *
 * @param {string} string
 * @returns {number[]}
 */
function parseVersionString(string) {
    let version = string.split('.', 3);

    for (let i = 0; i < 3; i++) {
        if (version[i]) {
            version[i] = parseInt(version[i]);
        } else {
            version[i] = 0;
        }
    }

    return version;
}

/**
 * Returns true if the current shell version is greater than the version string passed.
 *
 * @param {string} string Version string like 3.38.
 */
function versionGreaterOrEqual(string) {
    let current = parseVersionString(imports.misc.config.PACKAGE_VERSION);
    let version = parseVersionString(string);

    for (let i = 0; i < 3; i++) {
        if (current[i] < version[i]) {
            return false;
        }
    }

    return true;
}
