# test_playlist.py - simple assert-based tests
from playlist import playlist, add_song, remove_song, find_song, get_playlist_copy, replace_song

def run_checks():
    # Reset global for tests
    playlist[:] = ["A", "B", "C"]

    # add_song (no return)
    add_song("D")
    assert playlist == ["A", "B", "C", "D"], "add_song failed"

    # remove_song returns True when present, False otherwise
    assert remove_song("B") is True and playlist == ["A", "C", "D"], "remove_song failed for present item"
    assert remove_song("X") is False, "remove_song failed for absent item"

    # find_song
    assert find_song("A") == 0
    assert find_song("D") == 2
    assert find_song("Z") == -1

    # get_playlist_copy returns a copy, mutation of copy should not affect global
    copy = get_playlist_copy()
    copy.append("X")
    assert "X" not in playlist, "get_playlist_copy returned reference, not a copy"

    # replace_song
    playlist[:] = ["one", "two", "three"]
    result = replace_song("two", "2")
    assert result == (1, "2")
    assert playlist[1] == "2"
    assert replace_song("nope", "x") is None

    print("All tests passed.")

if __name__ == "__main__":
    run_checks()
