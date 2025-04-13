from typing import Literal,Union,List, Tuple
from pathlib import Path

def play_audio(audio_path:Union[Path,str],
               engine:Literal["auto","simpleaudio","pydub","playsound"] = "auto") -> None:
    """
    
    provided user with multiple option of packages for playing audio

    Parameters
    ----------
    audio_path : Union[Path,str]
        DESCRIPTION.
    engine : Literal["auto","simpleaudio","pydub","playsound"], optional
        DESCRIPTION. The default is "auto".

    Returns
    -------
    None.

    """
    # fix bug in case users don't install simpleaudio
    
    try:
        from pydub import AudioSegment
        from pydub.playback import play
        audio = AudioSegment.from_mp3(str(audio_path))
    except:
        pass

    try:
        import simpleaudio as sa
        # simpleaudio requires Microsoft Visual C++ 14.0.
        #  Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
        wave_obj = sa.WaveObject.from_wave_file(str(audio_path))
    except:
        pass
    
    
    if engine in ["auto"]:
        try:
            from playsound import playsound
            # playsound
            playsound(str(audio_path))
        except:
            try:
                # simpleaudio
                play_obj = wave_obj.play()
            except:
                # pydub
                play(audio)
                
    elif engine in ["simpleaudio"]:
        import simpleaudio as sa
        play_obj = wave_obj.play()
    elif engine in ["pydub"]:
        play(audio)
    elif engine in ["playsound"]:
        from playsound import playsound
        playsound(str(audio_path))


def atempo_chain(target_speed: float, max_chain_len: int = 5, tol: float = 1e-4) -> list[float]:
    
    """
    Generates a list of atempo values (each between 0.5 and 2.0) that multiply
    to approximate the given target speed.

    Parameters
    ----------
    target_speed : float
        Desired playback speed (e.g., 0.42).
    max_chain_len : int
        Maximum number of filters to try chaining.
    tol : float
        Acceptable tolerance between product and target speed.

    Returns
    -------
    List[float]
        A list of atempo values to use in FFmpeg.
    """
    # atempo only support value from 0.5 to 2.0
    # not tested
    if not target_speed > 0:
        raise ValueError("Speed must be a positive number.")

    def search_chain(current_product, chain):
        if abs(current_product - target_speed) < tol:
            return chain
        if len(chain) >= max_chain_len:
            return None
        for val in [x / 100 for x in range(50, 201)]:
            new_product = current_product * val
            if new_product > target_speed * (1 + tol):
                continue
            result = search_chain(new_product, chain + [val])
            if result:
                return result
        return None

    result = search_chain(1.0, [])
    if not result:
        raise ValueError(f"Could not approximate {target_speed}x speed within {max_chain_len} filters.")
    return result

del Literal,Union,List, Tuple