TARGET = out

IDIR = .
SDIR = .
ODIR = .

SRC = $(wildcard $(SDIR)/*.cpp)
OBJ = $(SRC:$(SDIR)/%.c=$(ODIR)/%.o)

CXX = g++
CXXFLAGS = -I$(IDIR)
CFLAGS += -Wall
PJLIBS =  -L../lib -L./usr/local/lib
INCLUDE = -I../include -I../pjproject/pjsip/include -I../pjproject/pjlib/include -I../pjproject/pjlib-util/include -I../pjproject/pjmedia/include -I../pjproject/pjnath/include
LIBS = -lg7221codec -lgsmcodec -lilbccodec -lpj -lpjsip-simple -lpjsip-ua -lpjsip -lpjsua -lpjsua2 -lpjlib-util -lpjmedia-audiodev -lresample -lspeex -lsrtp -lwebrtc -lyuv -lpjmedia-codec -lpjmedia-videodev -lpjmedia -lpjnath


$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) $(INCLUDE) $(PJLIBS) $^ $(LIBS) -o $@ 

$(ODIR)/%.o: $(SDIR)/%.c
	$(CXX) $(CXXFLAGS) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(TARGET)