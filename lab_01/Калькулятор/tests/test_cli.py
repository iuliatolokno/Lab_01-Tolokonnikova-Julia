import subprocess


def test_CLI_division_by_zero():
    result = subprocess.run(
        ["python", "-m", "toolkit", "calc", "43 / 0"],
        capture_output=True,
        text=True,
    )


    assert result.returncode != 0
    assert result.stderr != ""


def test_CLI_unmatched_units():
    result = subprocess.run(
        ["python", "-m", "toolkit", "convert", "22", "--from", "kg", "--to", "k"],
        capture_output=True,
        text=True,
    )

    assert result.returncode != 0
    assert "error" in result.stderr.lower() or "failed" in result.stderr.lower()
