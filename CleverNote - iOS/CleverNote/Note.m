//
//  Note.m
//  CleverNote
//
//  Created by Daniel Koehler on 18/10/2014.
//  Copyright (c) 2014 DanielKoehler. All rights reserved.
//

#import "Note.h"

@implementation Note

-(id) initWithJSONEncodedRepresentation:(NSDictionary *)json {
    
    // ASSIGNATION - Wait for API endpoints
    
    self.guid;
    self.title;	//string
    self.content;	//string
    self.contentHash;	//string
    self.contentLength;	//i32
    
    self.created;	//Timestamp
    self.updated ;	//Timestamp
    self.deleted;	//Timestamp
    self.active;	//bool
    self.updateSequenceNum;	//i32
    self.notebookGuid;	//string
    self.tagGuids;	//list<Guid>
    self.resources;	//list<Resource>
    //@property (strong, nonatomic) attributes	NoteAttributes
    self.tagNames;
    
    
    return self;
    
}

-(id) testNote {

    
    self.guid = @"1";
    self.title = @"Test Note";	//string
    self.content = @"Massive evernote file!!";	//string
    self.updated = [NSDate dateWithTimeIntervalSince1970:1203849];
    self.tags = @[@"Computer Science", @"Networking", @"Needs Revising"];
    
    return self;
    
}

@end
