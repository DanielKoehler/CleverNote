//
//  CleverNote.m
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import "CleverNote.h"
#import "AFNetworking.h"

#define kAPI_SCHEME @"http"
#define kAPI_PORT 3000
#define kAPI_HOST @"192.168.0.10"

@implementation CleverNote

-(id) init {
    
    if (self = [super init])
    {
        self.urlBuilder = [NSURLComponents alloc];
        [self.urlBuilder setPort:[NSNumber numberWithInt:8000]];
        [self.urlBuilder setScheme:kAPI_SCHEME];
        [self.urlBuilder setHost:kAPI_HOST];
        
    }
    return self;
}

-(void) loadNotes {
    
    // AFNEtworking Request
    
    
}

@end
