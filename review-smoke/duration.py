"""Standalone duration helper for the roborev publication test PR.

This module is not connected to OBS or imported by production scripts.
"""


def frames_to_seconds(frame_count: int, frames_per_second: int) -> float:
    """Convert a frame count to seconds, preserving partial seconds."""
    if frame_count < 0:
        raise ValueError("frame_count must be nonnegative")
    if frames_per_second <= 0:
        raise ValueError("frames_per_second must be positive")
    return frame_count / frames_per_second
