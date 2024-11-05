import sys

class VocalRange:
    """ Pitch 범위를 다루는 클래스 """
    note_to_midi = {
        'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
        'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
    }

    def __init__(self, min_note, max_note):
        self.min_note = min_note
        self.max_note = max_note
        self.min_midi = self.note_str_to_midi(min_note)
        self.max_midi = self.note_str_to_midi(max_note)

    def note_str_to_midi(self, note_str):
        note = note_str[:-1]
        octave = int(note_str[-1])
        return (octave + 1) * 12 + self.note_to_midi[note]

    @staticmethod
    def midi_to_note_name(midi_value):
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        octave = int((midi_value // 12) - 1)
        note = note_names[int(midi_value % 12)]
        return f"{note}{octave}"

    def get_range(self):
        return (self.min_note, self.max_note)

    def get_midi_range(self):
        return (self.min_midi, self.max_midi)


class KeyShiftCalculator:
    """ 
    song, user range 순서대로 넣으면 key shift 값과 octave shift 값을 계산함.
    input:
        song range (str, str)
        user range (str, str)
    output:
        semitone shift (int)
        octaves shifted (int)    
    """
    note_to_midi = VocalRange.note_to_midi

    def note_str_to_midi(self, note_str):
        note = note_str[:-1]
        octave = int(note_str[-1])
        return (octave + 1) * 12 + self.note_to_midi[note]

    def calculate_key_shift(self, song_range, user_range):
        song_low, song_high = [self.note_str_to_midi(note) for note in song_range]
        user_low, user_high = [self.note_str_to_midi(note) for note in user_range]
        
        assert song_high >= song_low and user_high >= user_low, "Range should be listed in right order: '(low, high)'"

        how_high = song_high - user_high
        total_shift = -how_high  # The initial required shift

        # Calculate the semitone shift within -6 to 6
        s = ((total_shift + 6) % 12) - 6

        # Calculate the number of octaves shifted
        k = (total_shift - s) // 12

        return s, k


def get_adjustment_message(key_shift, octave_shift):
    """키 조정값을 사용자가 이해하기 쉬운 메시지로 변환"""
    shift_direction = '높임' if key_shift > 0 else '낮춤'
    octave_direction = '올려' if octave_shift > 0 else '낮춰'

    if key_shift == 0 and octave_shift == 0:
        return "원래 키 그대로 부르세요"
    elif octave_shift == 0:
        return f"{abs(key_shift)}번 음정 {shift_direction} 버튼을 누르세요."
    else:
        return (f"{abs(key_shift)}번 음정 {shift_direction} 버튼을 누르고, "
               f"{abs(octave_shift)} 옥타브 {octave_direction} 부르세요.")


def main():
    # 키 조정 계산기 초기화
    calculator = KeyShiftCalculator()

    # 테스트용 데이터
    test_cases = [
        {
            'song_title': '너의 모든순간',
            'song_range': ('C3', 'G4'),
            'user_range': ('E2', 'A#3'),
        },
        {
            'song_title': '내가 아니라도',
            'song_range': ('D3', 'A4'),
            'user_range': ('E2', 'A#3'),
        },
        {
            'song_title': '사랑하지 않아서 그랬어',
            'song_range': ('B2', 'F4'),
            'user_range': ('E2', 'A#3'),
        }
    ]

    print("\n=== 노래 키 조정 추천 시스템 ===")
    print(f"사용자 음역대: {test_cases[0]['user_range']}\n")

    for case in test_cases:
        print(f"노래: {case['song_title']}")
        print(f"노래 음역대: {case['song_range']}")
        
        try:
            key_shift, octave_shift = calculator.calculate_key_shift(
                case['song_range'],
                case['user_range']
            )
            message = get_adjustment_message(key_shift, octave_shift)
            print(message + "\n")
            
        except AssertionError as e:
            print(f"오류: {str(e)}\n")
        except Exception as e:
            print(f"처리 중 오류가 발생했습니다: {str(e)}\n")


if __name__ == "__main__":
    main()