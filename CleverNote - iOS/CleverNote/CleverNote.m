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
    
    [self.urlBuilder setPath:[NSString stringWithFormat:@"/api/evernotey"]];
    NSURL *url = [self.urlBuilder URL];
    
    
    AFHTTPRequestOperationManager *manager = [AFHTTPRequestOperationManager manager];
    [manager GET:url parameters:nil success:^(AFHTTPRequestOperation *operation, id responseObject) {
        
        NSLog(@"JSON: %@", responseObject);
        
        // Parse all as notes.
        
    } failure:^(AFHTTPRequestOperation *operation, NSError *error) {
        
        NSLog(@"Error: %@", error);
   
    }];
    
    
}

+ (instancetype) singleton {
    static id singletonInstance = nil;
    if (!singletonInstance) {
        static dispatch_once_t onceToken;
        dispatch_once(&onceToken, ^{
            singletonInstance = [[super allocWithZone:NULL] init];
        });
    }
    return singletonInstance;
}

+ (id) allocWithZone:(NSZone *)zone {
    return [self singleton];
}

- (id) copyWithZone:(NSZone *)zone {
    return self;
}

@end
