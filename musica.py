import pygame.midi
import time
import threading

class Musica:
    def __init__(self, notas):
        self.notas = notas
        self.volume_global = 1  # Volume padrão (0.0 a 1.0)
        self._inicializar_midi()
        self.is_playing = False
        self.is_paused = False
        self.playback_thread = None
        self.pause_event = threading.Event()
        self.pause_event.set()

    def _inicializar_midi(self):
        if not pygame.midi.get_init():
            pygame.midi.init()
        if pygame.midi.get_count() > 0:
            self.player = pygame.midi.Output(0)
        else:
            raise Exception("Nenhum dispositivo MIDI disponível")

    def _reinicializar_midi(self):
        self.fechar()
        self._inicializar_midi()

    def set_volume(self, volume):
        self.volume_global = max(0.0, min(1.0, volume))


    def _playback(self):
            self.is_playing = True
            try:
                for nota in self.notas:
                    if not self.is_playing:
                        break
                    self.pause_event.wait()

                    if nota.nota != ' ':
                        midi_note = self._converter_nota_para_midi(nota.nota) + (12 * nota.oitava)
                        velocity = int(127 * min(nota.volume * self.volume_global, 1.0))

                        self.player.set_instrument(nota.instrumento)
                        self.player.note_on(midi_note, velocity)

                        time.sleep(60 / nota.bpm)

                        self.player.note_off(midi_note, velocity)
                    else:
                        time.sleep(60 / nota.bpm)
            finally:
                self.is_playing = False


    def _converter_nota_para_midi(self, nota):
        mapa_notas = {
            'A': 69, 'B': 71, 'C': 60, 'D': 62,
            'E': 64, 'F': 65, 'G': 67, 'H': 72,
        }
        return mapa_notas.get(nota.upper(), 60)

    def reproduzir(self):
        if self.is_playing:
            if not self.pause_event.is_set():
                self.pause_event.set()
                self.is_paused=False
                return
            else:
                return
        else:
            self._reinicializar_midi()
            self.is_playing = True
            self.pause_event.set()
            self.playback_thread = threading.Thread(target=self._playback)
            self.playback_thread.start()
            self.is_paused=False

    def pausar(self):
        if self.is_playing and self.pause_event.is_set():
            self.pause_event.clear()
            self.is_paused = True

    def resetar(self):
        self.pause_event.set()
        self.parar()
        self.is_paused= False
        self.reproduzir()
        

    def parar(self):
        self.is_playing = False
        if self.playback_thread and self.playback_thread.is_alive():
            if threading.current_thread() != self.playback_thread:
                self.playback_thread.join()

    def fechar(self):
        self.parar()
        if hasattr(self, 'player') and self.player:
            self.player.close()
            self.player = None
        if pygame.midi.get_init():
            pygame.midi.quit()
    