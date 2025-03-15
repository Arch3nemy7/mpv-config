from vsdenoise import nl_means
from vsrgtools import contrasharpening
from vstools import set_output

den = nl_means(video_in, strength=1.25, planes=0)  # type:ignore
csharp = contrasharpening(den, video_in)  # type:ignore

set_output(csharp)
