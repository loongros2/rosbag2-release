import rosbag2_py._compression_options
import rosbag2_py._storage
from typing import overload

class SequentialCompressionWriter:
    def __init__(self, arg0: rosbag2_py._compression_options.CompressionOptions) -> None: ...
    def create_topic(self, arg0: rosbag2_py._storage.TopicMetadata) -> None: ...
    def open(self, arg0: rosbag2_py._storage.StorageOptions, arg1: rosbag2_py._storage.ConverterOptions) -> None: ...
    def remove_topic(self, arg0: rosbag2_py._storage.TopicMetadata) -> None: ...
    def split_bagfile(self) -> None: ...
    def take_snapshot(self) -> bool: ...
    @overload
    def write(self, arg0: str, arg1: str, arg2: int) -> None: ...
    @overload
    def write(self, arg0: str, arg1: str, arg2: int, arg3: int) -> None: ...

class SequentialWriter:
    def __init__(self) -> None: ...
    def close(self) -> None: ...
    def create_topic(self, arg0: rosbag2_py._storage.TopicMetadata) -> None: ...
    def open(self, arg0: rosbag2_py._storage.StorageOptions, arg1: rosbag2_py._storage.ConverterOptions) -> None: ...
    def remove_topic(self, arg0: rosbag2_py._storage.TopicMetadata) -> None: ...
    def split_bagfile(self) -> None: ...
    def take_snapshot(self) -> bool: ...
    @overload
    def write(self, arg0: str, arg1: str, arg2: int) -> None: ...
    @overload
    def write(self, arg0: str, arg1: str, arg2: int, arg3: int) -> None: ...

def get_registered_compressors() -> Set[str]: ...
def get_registered_serializers() -> Set[str]: ...
def get_registered_writers() -> Set[str]: ...
