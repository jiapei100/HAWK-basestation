"""autogenerated by genmsg_py from newedge.msg. Do not edit."""
import roslib.message
import struct


class newedge(roslib.message.Message):
  _md5sum = "4dc59ec3b0c54addb13a6d290b0c5b3c"
  _type = "ic2020_toro/newedge"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Index of Keyframes
uint32 prime_keyframe
uint32 obs_keyframe

# Rotation and Translation
float32[] rot
float32[] trans

"""
  __slots__ = ['prime_keyframe','obs_keyframe','rot','trans']
  _slot_types = ['uint32','uint32','float32[]','float32[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.
    
    The available fields are:
       prime_keyframe,obs_keyframe,rot,trans
    
    @param args: complete set of field values, in .msg order
    @param kwds: use keyword arguments corresponding to message field names
    to set specific fields. 
    """
    if args or kwds:
      super(newedge, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.prime_keyframe is None:
        self.prime_keyframe = 0
      if self.obs_keyframe is None:
        self.obs_keyframe = 0
      if self.rot is None:
        self.rot = []
      if self.trans is None:
        self.trans = []
    else:
      self.prime_keyframe = 0
      self.obs_keyframe = 0
      self.rot = []
      self.trans = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    @param buff: buffer
    @type  buff: StringIO
    """
    try:
      _x = self
      buff.write(_struct_2I.pack(_x.prime_keyframe, _x.obs_keyframe))
      length = len(self.rot)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.rot))
      length = len(self.trans)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.trans))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    @param str: byte array of serialized message
    @type  str: str
    """
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.prime_keyframe, _x.obs_keyframe,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.rot = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.trans = struct.unpack(pattern, str[start:end])
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    @param buff: buffer
    @type  buff: StringIO
    @param numpy: numpy python module
    @type  numpy module
    """
    try:
      _x = self
      buff.write(_struct_2I.pack(_x.prime_keyframe, _x.obs_keyframe))
      length = len(self.rot)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.rot.tostring())
      length = len(self.trans)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.trans.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    @param str: byte array of serialized message
    @type  str: str
    @param numpy: numpy python module
    @type  numpy: module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 8
      (_x.prime_keyframe, _x.obs_keyframe,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.rot = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.trans = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      return self
    except struct.error as e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

_struct_I = roslib.message.struct_I
_struct_2I = struct.Struct("<2I")