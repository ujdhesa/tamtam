from EventPlayer import EventPlayer
from Framework.CSound.CSoundConstants import CSoundConstants

class TrackPlayerBase( EventPlayer ):
    #-----------------------------------
    # initialization
    #-----------------------------------
    def __init__( self, getTempoCallback, getBeatsPerPageCallback, playTickCallback, volumeFunctions, trackIDs ):
        EventPlayer.__init__( self, getTempoCallback, getBeatsPerPageCallback, playTickCallback )
        
        self.trackIDs = set( trackIDs )
        self.selectedTrackIDs = set()
        self.mutedTrackIDs = set()
        self.trackInstruments = {} #maps trackIDs to instrumentNames

        if len( trackIDs ) == 4:
            self.trackInstruments[ 0 ] = CSoundConstants.FLUTE
            self.trackInstruments[ 1 ] = CSoundConstants.HHC
            self.trackInstruments[ 2 ] = CSoundConstants.SNARE
            self.trackInstruments[ 3 ] = CSoundConstants.BD
        else:
            for trackID in trackIDs:
                self.trackInstruments[ trackID ] = CSoundConstants.FLUTE
        
    #-----------------------------------
    # toggle methods
    #-----------------------------------        
    def toggleSelectTrack( self, trackID ):
        self.toggle( self.selectedTrackIDs, trackID )
        self.update()
    
    def toggleMuteTrack( self, trackID ):
        self.toggle( self.mutedTrackIDs, trackID )
        self.update()
        
    def toggle( self, set, object ):
        if object in set:
            set.discard( object )
        else:
            set.add( object )
            
    #-----------------------------------
    # misc methods
    #-----------------------------------                    
    def getActiveTrackIDs( self ):
        if len( self.selectedTrackIDs ) != 0:
            return self.selectedTrackIDs
        else:
            return self.trackIDs.difference( self.mutedTrackIDs )

    # data is a tuple ( trackID, instrumentName )
    def setInstrument( self, data ):
        trackID = data[0]
        instrument = data[1]
        for event in self.getEvents( trackID ):
            event.instrument = instrument

        self.trackInstruments[ trackID ] = instrument
        
    def update( self ):
       raise NotImplementedError